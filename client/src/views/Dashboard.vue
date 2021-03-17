<template>
    <div fluid class="pa-10">

        <v-row>
            <v-col cols="8">
                <v-card>
                    <v-card-text>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="4">
                <v-card>
                    <v-card-text>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-text>

                        <scheduler :scheduledData="scheduledProjectData" :headers="fortnights"></scheduler>

                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

    </div>
</template>
<style>

</style>
<script>
    import Scheduler from '../components/Scheduler.vue';
    export default {
        components: { Scheduler },
        data() {
            return {
                fortnights: [],
                roles: [],

                scheduledProjectData: {},
            }
        },

        created() {
            this.loadFortnights();
            this.loadRoles();

            this.loadScheduledProjectData();
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
            loadScheduledProjectData() {
                this.$api.get("/projects/schedule").then(res => {
                    this.scheduledProjectData = res.data.schedule;

                    console.log(res.data.schedule)
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
            }
        }
    }
</script>
