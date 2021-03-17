<template>
    <div fluid class="pa-10">

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-text>
                        <v-data-table :headers="headers" :items="roles">
                            <template v-slot:item.actions="{ item }">
                                <v-icon class="mr-2 text-primary" @click="editItem(item)">mdi-pencil</v-icon>
                                <v-icon @click="deleteItem(item)" color="red">mdi-delete</v-icon>
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
                            <v-col cols="8">
                                <v-text-field v-model="roleName" outlined label="Nome" hide-details></v-text-field>
                            </v-col>
                            <v-col cols="4">
                                <v-text-field v-model="roleCapacity" outlined label="Capacidade" hide-details type="number"></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" class="d-flex">
                                <v-spacer></v-spacer>

                                <v-btn v-if="editingItem" color="red" dark class="mr-2" @click="cancelEdit()">Cancelar</v-btn>

                                <v-btn v-if="!editingItem" class="block-primary" @click="addRole()">Adicionar</v-btn>
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
                <v-card-text>Tem certeza que quer excluir o cargo <b>{{ deletingItem.name }}</b> ?</v-card-text>
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
                headers: [
                    { text: "Nome", value: "name" },
                    { text: "Capacidade", value: "capacity" },
                    { text: "", value: "actions", sortable: false }
                ],

                roles: [],

                roleName: "",
                roleCapacity: null,

                editingItem: null,

                deletingItem: null,
                dialogDelete: false,
            }
        },

        created() {
            this.loadRoles()
        },

        methods: {
            loadRoles() {
                this.$api.get("/roles").then(res => {
                    const data = res.data;

                    this.roles = data.roles;
                })
            },
            validateData() {
                if (!this.roleName || !this.roleName.length) {
                    this.$store.commit("setInfo", {
                        message: "Nome é obrigatório",
                        success: false
                    });
                    return false;
                }

                if (!this.roleCapacity || this.roleCapacity && this.roleCapacity <= 0) {
                    this.$store.commit("setInfo", {
                        message: "Capacidade precisa ser maior que zero",
                        success: false
                    });
                    return false;
                }

                return true;
            },
            addRole() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.roleName,
                    capacity: this.roleCapacity
                }

                this.$api.post("/roles", payload).then(res => {
                    this.loadRoles();
                    this.cancelEdit();
                })
            },
            editItem(item) {
                this.editingItem = item;

                this.roleName = item.name;
                this.roleCapacity = item.capacity;
            },
            deleteItem(item) {
                this.deletingItem = item;

                this.dialogDelete = true;
            },
            confirmDeleteItem() {
                this.$api.delete(`/roles/${this.deletingItem._id}`).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.roles = this.roles.filter(el => {
                        if (el._id === this.deletingItem._id) return false;
                        return true;
                    })
                })
            },
            confirmEditItem() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.roleName,
                    capacity: this.roleCapacity,
                };

                this.$api.put(`/roles/${this.editingItem._id}`, payload).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.roles.map(el => {
                        if (el._id === this.editingItem._id) {
                            for (let k in payload) {
                                el[k] = payload[k];
                            }
                        }
                        return el;
                    })

                    this.cancelEdit();
                })
            },
            cancelEdit() {
                this.editingItem = null;
                this.roleName = "";
                this.roleCapacity = null;
            },
            getEditTitle() {
                return !this.editingItem ? "Adicionar novo cargo" : `Editar cargo (${this.editingItem.name})`;
            }
        }
    }
</script>
