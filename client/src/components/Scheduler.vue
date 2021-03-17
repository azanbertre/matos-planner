<template>
    <div fluid id="schedule">
        <div class="g-wrapper">
            <div class="g-header">
                <div v-for="k in headers" :key="k.name" class="g-cell">
                    <span>{{ k.name.substr(0, k.name.length - 7) }}</span>
                </div>
            </div>
            <div class="g-row" v-for="k in scheduledData" :key="k.name">
                <div class="g-schedule block-primary" :style="getScheduleStyle(k)">
                    {{ k.name }}
                </div>
            </div>

            <div v-for="(k, i) in headers" :key="i" class="g-vertical-line" :style="`transform: translate(calc(10em * ${i}))`"></div>
        </div>
    </div>
</template>
<style>
    #schedule {
        overflow-x: scroll;
        overflow-y: hidden;
        position: relative;

        /* display: inline-block; */
    }

    .g-wrapper {
        display: inline-block;
    }

    .g-header {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;

        min-height: 25px;

        /* background-color: #667280; */
        background-color: #f3f4f5;
    }

    .g-row {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;

        border-bottom: 1px solid #e9eaeb;

        width: 100%;

        min-height: 50px;
    }

    .g-row:last-child {
        border-bottom: none !important;
    }

    .g-cell {
        display: flex;
        align-items: center;
        justify-content: center;

        min-width: 10em;
        width: 10em;
        text-align: center;
    }

    .g-schedule {
        position: absolute;
        width: 10em;
        height: 40px;

        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;

        z-index: 5;
    }

    .g-vertical-line {
        position: absolute;
        border-right: 1px solid #e9eaeb;

        height: 100%;

        top: 0;

        width: 10em;
    }

    .g-vertical-line:last-child {
        border-right: none;
    }
</style>
<script>
    export default {
        props: ["headers", "scheduledData"],
        created() {

        },
        data() {
            return {}
        },
        computed: {

        },
        methods: {
            getScheduleStyle(item) {
                return `transform: translate(calc(10em * ${item.start} + 5px), 5px); width: calc(10em * ${Math.max(item.end - item.start, 1)} - 10px)`;
            }
        },
    };
</script>

<style></style>
