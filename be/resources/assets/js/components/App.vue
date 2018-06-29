<template>
    <div class="app">
        <Header v-bind:showLogout="true"></Header>
        <main>
            <section class="left">
                <Table></Table>
            </section>
            <section
                    :class="{fixed: flag, normal: !flag}"
                    class="right">
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
                flag: false,
                compareHeight: null
            }
        },
        components: {
            Table,
            Header,
            AdminCenter
        },
        methods: {
            handleScroll() {
                let scrollTop = document.body.scrollTop + document.documentElement.scrollTop;
                this.fixed(scrollTop);
            },

            setCompareHeight() {
                let header = document.querySelector('#header');
                this.compareHeight = parseInt(window.getComputedStyle(header).getPropertyValue("height"));
            },

            fixed(scrollTop) {
                console.log(this.compareHeight);
                if (scrollTop > this.compareHeight) {
                    console.log(scrollTop);
                    this.flag = true;
                } else {
                    this.flag = false;
                }
            }
        },
        mounted(){
            this.setCompareHeight();
            window.addEventListener('scroll', this.handleScroll); // 添加滚动事件
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
        border: 2px solid red;

    }

    .app .fixed {
        position: fixed;
        top: 0px;
        right: 0;
    }

    .app .normal{
        position: static;
        float: right;
    }
</style>