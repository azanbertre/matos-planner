<template>
    <div fluid>

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
            }
        }
    }
</script>
