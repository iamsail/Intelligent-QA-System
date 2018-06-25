<template>
    <div class="app">
        <Header v-bind:showLogout="true"></Header>
        <main>
            <section class="left">
                <Table></Table>
            </section>
            <section class="right">
                <AdminCenter></AdminCenter>
            </section>
        </main>
    </div>
</template>

<script>
    import Header from './common/Header'
    import Table from './Table'
    import AdminCenter from './AdminCenter'
    export default {
        name: "App",
        data() {
            return {
            }
        },
        components: {
            Table,
            Header,
            AdminCenter
        },
        methods: {

        },
        mounted(){
        }
    }
</script>

<style scoped>
    .app {}
    .app .left{
        display: inline-block;
        width: 80%;
    }

    .app .right{
        width: 20%;
        min-height: 900px;
        height: 100%;
        float: right;
        border: 2px solid red;
    }
</style>