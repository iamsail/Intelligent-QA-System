<template>
    <div class="header">
        <el-menu
                :default-active="activeIndex"
                class="el-menu-demo"
                mode="horizontal"
                @select="handleSelect"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
            <el-menu-item index="1">智能对话系统</el-menu-item>
            <el-menu-item index="2" class="right">{{username}}</el-menu-item>
            <el-menu-item index="3" class="right" @click="logout()"　v-if="show">注销</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Header",
        props:["showLogout"],
        data() {
            return {
                activeIndex: '1',
                username: "游客",
                show: false
            };
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },


            /**
             * 获取用户名
             */
            getUsername() {
                axios.get('/username')
                    .then((response)  =>{
                        this.username = response.data;
                    })
                    .catch((error) => {

                    });
            },


            /**
             * 用户登出
             */
            logout() {
                axios.get('/logout')
                    .then((response)  =>{
                        this.username = response.data;
                        window.location.href = '/login';
                    })
                    .catch((error) => {

                    });
            }
        },
        mounted() {
            this.getUsername();
            this.show = this.showLogout;
        }
    }
</script>

<style scoped>
    .header .right {
        float: right;
    }
</style>