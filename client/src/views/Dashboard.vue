<template>
    <div fluid class="pa-10">

        <v-row>
            <v-col cols="8">
                <v-card height="300px">
                    <v-card-text>
                        <chart v-if="chartData" :chart-data="chartData" :options="chartOptions" :styles="{positions: 'relative', height: 'calc(300px - 32px)'}"></chart>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="4">
                <v-card height="300px">
                    <v-card-title class="d-flex justify-center">
                        <div class="text-primary">Capacidade Atual</div>
                    </v-card-title>
                    <v-card-text v-if="currentCapacity && currentCapacity.capacity" class="d-flex flex-column justify-center">

                        <v-row class="mt-5">
                            <v-col cols="12">
                                <div style="position: relative; text-align: center;">
                                    <span class="text-primary text-h1 font-weight-bold">
                                        {{ currentCapacity.capacity.free }}
                                    </span>
                                    <span class="text-primary" style="position: absolute; bottom: 10px;">
                                        Livre
                                    </span>
                                </div>
                            </v-col>
                        </v-row>

                        <v-row class="text-primary text-h6 mt-10" style="text-align: center;">
                            <v-col cols="6">
                                Total | {{ currentCapacity.capacity.total }}
                            </v-col>
                            <v-col cols="6">
                                Usado | {{ currentCapacity.capacity.used }}
                            </v-col>
                        </v-row>
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

        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-text>
                        <scheduler :scheduledData="scheduledMemberData" :headers="fortnights"></scheduler>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

    </div>
</template>
<style>

</style>
<script>
    import Chart from '../components/Chart.js';
    import Scheduler from '../components/Scheduler.vue';

    export default {
        components: { Scheduler, Chart },
        data() {
            return {
                fortnights: [],
                roles: [],

                capacity: [],
                currentCapacity: {},

                scheduledProjectData: {},
                scheduledMemberData: {},

                chartData: null,
                chartOptions: null,

            }
        },

        mounted() {

        },

        created() {
            this.loadFortnights();
            this.loadRoles();

            this.loadScheduledProjectData();
            this.loadScheduledMemberData();
            this.loadCapacity();
        },

        methods: {

            fillData () {
                this.chartData = {
                    labels: this.fortnights.map(el => el.name),
                    datasets: [
                        {
                            label: 'Usado',
                            backgroundColor: '#f87979',
                            data: this.capacity.map(el => el.capacity.used)
                        },
                        {
                            label: 'Livre',
                            backgroundColor: '#58E144',
                            data: this.capacity.map(el => el.capacity.free)
                        },
                        {
                            label: 'Total',
                            backgroundColor: '#33395E',
                            data: this.capacity.map(el => el.capacity.total)
                        },
                    ]
                }

                this.chartOptions = {
                    responsive: true,
                    maintainAspectRatio: false
                }
            },
            getRandomInt () {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            },

            loadFortnights() {
                this.$api.get("/projects/fortnights", false).then(res => {
                    this.fortnights = res.data.fortnights;
                })
            },
            loadRoles() {
                this.$api.get("/roles", false).then(res => {
                    this.roles = res.data.roles;
                })
            },
            loadScheduledProjectData() {
                this.$api.get("/projects/schedule", false).then(res => {
                    this.scheduledProjectData = res.data.schedule;
                })
            },
            loadScheduledMemberData() {
                this.$api.get("/members/schedule", false).then(res => {
                    this.scheduledMemberData = res.data.schedule;
                })
            },
            loadCapacity() {
                this.$api.get("/capacity", false).then(res => {
                    this.capacity = res.data.capacity;
                    this.currentCapacity = res.data.currentCapacity;

                    this.fillData();
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
