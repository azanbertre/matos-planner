<template>
    <div fluid class="pa-10">

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-text>
                        <v-data-table :headers="headers" :items="members">
                            <template v-slot:item.actions="{ item }">
                                <v-icon class="mr-2 text-primary" @click="editItem(item)">mdi-pencil</v-icon>
                                <v-icon @click="deleteItem(item)" color="red">mdi-delete</v-icon>
                            </template>

                            <template v-slot:item.capacity="{ item }">
                                <span v-if="!item.capacity_override">{{ item.role.capacity }}</span>
                                <span v-else>{{ item.capacity_override }}</span>
                            </template>

                            <template v-slot:item.fortnight_start.value="{ item }">
                                <span>{{ item.fortnight_start.name }}</span>
                            </template>

                            <template v-slot:item.fortnight_end.value="{ item }">
                                <span>{{ item.fortnight_end.name }}</span>
                            </template>
                        </v-data-table>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>
                        {{ getEditTitle() }}
                    </v-card-title>
                    <v-card-text>
                        <v-row>
                            <v-col cols="4">
                                <v-text-field v-model="memberName" outlined label="Nome" hide-details></v-text-field>
                            </v-col>
                            <v-col cols="4">
                                <v-text-field v-model="memberCapacity" outlined label="Capacidade (Vazio para usar do cargo)" hide-details type="number" placeholder="Deixar vazio para usar do cargo"></v-text-field>
                            </v-col>
                            <v-col cols="4">
                                <v-select v-model="memberRole" outlined label="Cargo" item-text="name" item-value="_id" :items="roles" hide-details></v-select>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="6">
                                <v-select v-model="memberStart" outlined label="Inicio" item-text="name" item-value="value" :items="filterFortnights(fortnights, memberStart, memberEnd, true)" hide-details></v-select>
                            </v-col>
                            <v-col cols="6">
                                <v-select v-model="memberEnd" outlined label="Final" item-text="name" item-value="value" :items="filterFortnights(fortnights, memberStart, memberEnd, false)" hide-details></v-select>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" class="d-flex">
                                <v-spacer></v-spacer>

                                <v-btn v-if="editingItem" color="red" dark class="mr-2" @click="cancelEdit()">Cancelar</v-btn>

                                <v-btn v-if="!editingItem" class="block-primary" @click="addMember()">Adicionar</v-btn>
                                <v-btn v-else class="block-primary" @click="confirmEditItem()">Editar</v-btn>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-dialog
            v-model="dialogDelete"
            persistent
            max-width="300"
            v-if="deletingItem"
        >
            <v-card>
                <v-card-title class="headline">
                    Excluir
                </v-card-title>
                <v-card-text>Tem certeza que quer excluir o membro <b>{{ deletingItem.name }}</b> ?</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        class="text-primary"
                        text
                        @click="dialogDelete = false"
                    >
                        Cancelar
                    </v-btn>
                    <v-btn
                        class="block-primary"
                        text
                        @click="confirmDeleteItem(); dialogDelete = false"
                    >
                        Excluir
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </div>
</template>

<style>

</style>

<script>
    export default {
        data() {
            return {
                fortnights: [],

                roles: [],

                memberStart: null,
                memberEnd: null,
                memberName: '',
                memberRole: null,
                memberCapacity: null,

                members: [],

                headers: [
                    { text: "Nome", value: "name" },
                    { text: "Cargo", value: "role.name" },
                    { text: "Capacidade", value: "capacity" },
                    { text: "Inicio", value: "fortnight_start.value" },
                    { text: "Final", value: "fortnight_end.value" },
                    { text: "", value: "actions", sortable: false }
                ],

                editingItem: null,

                deletingItem: null,
                dialogDelete: false,
            }
        },

        created() {
            this.loadFortnights();
            this.loadMembers();
            this.loadRoles();
        },

        methods: {
            loadFortnights() {
                this.$api.get("/projects/fortnights").then(res => {
                    this.fortnights = res.data.fortnights;
                })
            },
            filterFortnights(fortnights, start, end, isStart) {
                if (isStart && !end) return fortnights;
                if (!isStart && !start) return fortnights;

                if (isStart) {
                    return fortnights.filter(el => {
                        return el.value <= end;
                    })
                } else {
                    return fortnights.filter(el => {
                        return el.value >= start;
                    })
                }
            },
            loadRoles() {
                this.$api.get("/roles").then(res => {
                    const data = res.data;

                    this.roles = data.roles;
                })
            },
            loadMembers() {
                this.$api.get("/members").then(res => {
                    const data = res.data;

                    this.members = data.members;
                })
            },
            validateData() {
                if (!this.memberName || !this.memberName.length) {
                    this.$store.commit("setInfo", {
                        message: "Nome é obrigatório",
                        success: false
                    });
                    return false;
                }

                if (!this.memberStart || !this.memberEnd) {
                    this.$store.commit("setInfo", {
                        message: "Inicio e final são obrigatórios",
                        success: false
                    });
                    return false;
                }

                if (!this.memberRole) {
                    this.$store.commit("setInfo", {
                        message: "Cargo é obrigatório",
                        success: false
                    });
                    return false;
                }

                if ((this.memberCapacity != null && this.memberCapacity.length) && this.memberCapacity <= 0) {
                    this.$store.commit("setInfo", {
                        message: "Capacidade precisa ser maior que zero",
                        success: false
                    });
                    return false;
                }

                if (this.memberCapacity && !this.memberCapacity.length) {
                    this.memberCapacity = null;
                }

                return true;
            },
            addMember() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.memberName,
                    fortnight_start: this.memberStart,
                    fortnight_end: this.memberEnd,
                    role_id: this.memberRole,
                    capacity_override: this.memberCapacity
                }

                this.$api.post("/members", payload).then(res => {
                    this.loadMembers();
                    this.cancelEdit();
                })
            },
            editItem(item) {
                this.editingItem = item;

                this.memberName = item.name;
                this.memberStart = item.fortnight_start.value;
                this.memberEnd = item.fortnight_end.value;
                this.memberRole = item.role_id;
                this.memberCapacity = item.capacity_override;
            },
            deleteItem(item) {
                this.deletingItem = item;

                this.dialogDelete = true;
            },
            confirmDeleteItem() {
                this.$api.delete(`/members/${this.deletingItem._id}`).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.members = this.members.filter(el => {
                        if (el._id === this.deletingItem._id) return false;
                        return true;
                    })
                })
            },
            confirmEditItem() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.memberName,
                    fortnight_start: this.memberStart,
                    fortnight_end: this.memberEnd,
                    role_id: this.memberRole,
                    capacity_override: this.memberCapacity
                };

                this.$api.put(`/members/${this.editingItem._id}`, payload).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.members.map(el => {
                        if (el._id === this.editingItem._id) {
                            for (let k in payload) {
                                if (['fortnight_start', 'fortnight_end'].includes(k)) {
                                    el[k] = {
                                        name: this.fortnights.filter(el => el.value === payload[k])[0].name,
                                        value: payload[k]
                                    }
                                } else {
                                    el[k] = payload[k];
                                }
                            }
                        }
                        return el;
                    })

                    this.cancelEdit();
                })
            },
            cancelEdit() {
                this.editingItem = null;
                this.memberName = "";
                this.memberStart = null;
                this.memberEnd = null;
                this.memberRole = null;
                this.memberCapacity = null;
            },
            getEditTitle() {
                return !this.editingItem ? "Adicionar novo membro" : `Editar membro (${this.editingItem.name})`;
            }
        }
    }
</script>
