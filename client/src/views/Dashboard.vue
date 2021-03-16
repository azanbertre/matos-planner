<template>
    <div fluid>


        <v-card>
            <v-card-title>
                Projects
            </v-card-title>
            <v-card-text>
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="projectName" outlined label="Name" hide-details></v-text-field>
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

                        <v-btn class="block-primary" @click="addProject()">Adicionar</v-btn>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>

        <v-card>
            <v-card-title>
                Membros
            </v-card-title>
            <v-card-text>
                <v-row>
                    <v-col cols="8">
                        <v-text-field v-model="memberName" outlined label="Name" hide-details></v-text-field>
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

                        <v-btn class="block-primary" @click="addMember()">Adicionar</v-btn>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>

        <v-card>
            <v-card-title>
                Cargos
            </v-card-title>
            <v-card-text>
                <v-row>
                    <v-col cols="8">
                        <v-text-field v-model="roleName" outlined label="Name" hide-details></v-text-field>
                    </v-col>
                    <v-col cols="4">
                        <v-text-field v-model="roleCapacity" outlined label="Capacidade" hide-details type="number"></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12" class="d-flex">
                        <v-spacer></v-spacer>

                        <v-btn class="block-primary" @click="addRole()">Adicionar</v-btn>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>


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

                projectStart: null,
                projectEnd: null,
                projectName: '',

                roleName: '',
                roleCapacity: 0,

                memberName: '',
                memberStart: null,
                memberEnd: null,
                memberRole: null,
            }
        },

        created() {
            this.loadFortnights();
            this.loadRoles();
        },

        methods: {
            loadFortnights() {
                this.$api.get("/projects/fortnights").then(res => {
                    this.fortnights = res.data.fortnights;
                })
            },
            loadRoles() {
                this.$api.get("/roles").then(res => {
                    this.roles = res.data.roles;
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
            addProject() {

                if (!this.projectName || !this.projectName.length) {
                    return;
                }

                if (!this.projectStart || !this.projectEnd) {
                    return;
                }

                const payload = {
                    name: this.projectName,
                    start: this.projectStart,
                    end: this.projectEnd
                }

                this.$api.post("/projects", payload).then(res => {
                    console.log("adicionado");
                })
            },
            addMember() {
                if (!this.memberName || !this.memberName.length) {
                    return;
                }

                if (!this.memberStart || !this.memberEnd) {
                    return;
                }

                if (!this.memberRole) {
                    return;
                }

                const payload = {
                    name: this.memberName,
                    start: this.memberStart,
                    end: this.memberEnd,
                    role_id: this.memberRole
                }

                this.$api.post("/members", payload).then(res => {
                    const data = res.data;

                    this.$store.commit("setInfo", data);
                })
            },
            addRole() {

                if (!this.roleName || !this.roleName.length) {
                    return;
                }

                if (this.roleCapacity <= 0) {
                    return;
                }

                const payload = {
                    name: this.roleName,
                    capacity: this.roleCapacity
                }

                this.$api.post("/roles", payload).then(res => {
                    console.log("adicionado");
                })

            }
        }
    }
</script>
