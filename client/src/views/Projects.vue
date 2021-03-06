<template>
    <div fluid class="pa-10">

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-text>
                        <v-data-table :headers="headers" :items="projects">
                            <template v-slot:item.actions="{ item }">
                                <v-icon class="mr-2 text-primary" @click="editItem(item)">mdi-pencil</v-icon>
                                <v-icon @click="deleteItem(item)" color="red">mdi-delete</v-icon>
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
                            <v-col cols="8">
                                <v-text-field v-model="projectName" outlined label="Nome" hide-details></v-text-field>
                            </v-col>
                            <v-col cols="4">
                                <v-select v-model="projectType" outlined label="Tipo" :items="types" hide-details></v-select>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="6">
                                <v-select v-model="projectStart" outlined label="Inicio" item-text="name" item-value="value" :items="filterFortnights(fortnights, projectStart, projectEnd, true)" hide-details></v-select>
                            </v-col>
                            <v-col cols="6">
                                <v-select v-model="projectEnd" outlined label="Final" item-text="name" item-value="value" :items="filterFortnights(fortnights, projectStart, projectEnd, false)" hide-details></v-select>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" class="d-flex">
                                <v-spacer></v-spacer>

                                <v-btn v-if="editingItem" color="red" dark class="mr-2" @click="cancelEdit()">Cancelar</v-btn>

                                <v-btn v-if="!editingItem" class="block-primary" @click="addProject()">Adicionar</v-btn>
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
                <v-card-text>Tem certeza que quer excluir o projeto <b>{{ deletingItem.name }}</b> ?</v-card-text>
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
                projects: [],
                types: [
                    'Consultoria',
                    'Assessoria'
                ],

                projectStart: null,
                projectEnd: null,
                projectName: '',
                projectType: null,

                headers: [
                    { text: "Nome", value: "name" },
                    { text: "Tipo", value: "type" },
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
            this.loadProjects();
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
            loadProjects() {
                this.$api.get("/projects").then(res => {
                    const data = res.data;

                    this.projects = data.projects;
                })
            },
            validateData() {
                if (!this.projectName || !this.projectName.length) {
                    this.$store.commit("setInfo", {
                        message: "Nome é obrigatório",
                        success: false
                    });
                    return false;
                }

                if (!this.projectStart || !this.projectEnd) {
                    this.$store.commit("setInfo", {
                        message: "Inicio e final são obrigatórios",
                        success: false
                    });
                    return false;
                }

                if (!this.projectType) {
                    this.$store.commit("setInfo", {
                        message: "Projeto precisa de um tipo",
                        success: false
                    });
                    return false;
                }

                return true;
            },
            addProject() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.projectName,
                    type: this.projectType,
                    fortnight_start: this.projectStart,
                    fortnight_end: this.projectEnd
                }

                this.$api.post("/projects", payload).then(res => {
                    this.loadProjects();
                    this.cancelEdit();
                })
            },
            editItem(item) {
                this.editingItem = item;

                this.projectName = item.name;
                this.projectType = item.type;
                this.projectStart = item.fortnight_start.value;
                this.projectEnd = item.fortnight_end.value;
            },
            deleteItem(item) {
                this.deletingItem = item;

                this.dialogDelete = true;
            },
            confirmDeleteItem() {
                this.$api.delete(`/projects/${this.deletingItem._id}`).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.projects = this.projects.filter(el => {
                        if (el._id === this.deletingItem._id) return false;
                        return true;
                    })
                })
            },
            confirmEditItem() {

                if (!this.validateData()) return;

                const payload = {
                    name: this.projectName,
                    type: this.projectType,
                    fortnight_start: this.projectStart,
                    fortnight_end: this.projectEnd
                };

                this.$api.put(`/projects/${this.editingItem._id}`, payload).then(res => {
                    const data = res.data;
                    this.$store.commit("setInfo", data);

                    this.projects.map(el => {
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
                this.projectName = "";
                this.projectType = null;
                this.projectStart = null;
                this.projectEnd = null;
            },
            getEditTitle() {
                return !this.editingItem ? "Adicionar novo projeto" : `Editar projeto (${this.editingItem.name})`;
            }
        }
    }
</script>
