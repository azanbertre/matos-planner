<template>
    <v-snackbar v-model="$store.getters.info.show" timeout="3000" :color="color" top>

        {{ message }}

        <template v-slot:action="{ attrs }">
            <v-btn
                text
                v-bind="attrs"
                @click="$store.state.info.show = false"
            >
                Fechar
            </v-btn>

        </template>

    </v-snackbar>
</template>
<style>

</style>
<script>
    export default {
        data() {
            return {}
        },
        computed: {
            message() {
                return this.$store.getters.info.message;
            },
            color() {
                return this.$store.getters.info.color;
            }
        },
        methods: {

        },
    };
</script>

<style></style>
