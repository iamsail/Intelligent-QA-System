<template>
    <div>
        <Header v-bind:showLogout="true"></Header>
        <Table></Table>
    </div>
</template>

<script>
    import Header from './common/Header'
    import Table from './Table'
    export default {
        name: "App",
        data() {
            return {
            }
        },
        components: {
            Table,
            Header
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