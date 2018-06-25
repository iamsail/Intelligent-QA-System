<template>
    <div>
        <Table></Table>
    </div>
</template>

<script>
    import Table from './Table'
    export default {
        name: "App",
        data() {
            return {
            }
        },
        components: {
            Table
        },
        methods: {

        },
        mounted(){
        }
    }
</script>

<style scoped>
    .hello {
        font-size: 2em;
        color: green;
    }
</style>