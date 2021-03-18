<template>
    <div fluid id="schedule" v-dragscroll>
        <div class="g-wrapper">
            <div class="g-header">
                <div v-for="k in headers" :key="k.name" class="g-cell">
                    <span>{{ k.name.substr(0, k.name.length - 7) }}</span>
                </div>
            </div>
            <div class="g-row" v-for="k in scheduledData" :key="k.name">
                <div v-for="k in headers" :key="k.name" class="g-cell" style="opacity: 0.2">
                    <span>{{ k.name.substr(0, k.name.length - 7) }}</span>
                </div>
                <div class="g-schedule block-primary" :style="getScheduleStyle(k)">
                    <span style="left: 1em; position: absolute;" v-if="k.end - k.start > 4">{{ k.name }}</span>
                    <span v-if="(k.end - k.start) > 6 || (k.end - k.start) <= 4">{{ k.name }}</span>
                    <span style="right: 1em; position: absolute;" v-if="k.end - k.start > 4">{{ k.name }}</span>
                </div>
            </div>

            <div v-for="(k, i) in headers" :key="i" class="g-vertical-line" :style="`transform: translate(calc(7em * ${i}))`"></div>
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

        min-width: 8.75em;
        width: 8.75em;
        text-align: center;

        font-size: 0.8em;
    }

    .g-schedule {
        position: absolute;
        width: 7em;
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

        width: 7em;
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
                return `transform: translate(calc(7em * ${item.start} + 5px), 5px); width: calc(7em * ${Math.max((item.end - item.start) + 1, 1)} - 10px)`;
            }
        },
    };
</script>

<style></style>
