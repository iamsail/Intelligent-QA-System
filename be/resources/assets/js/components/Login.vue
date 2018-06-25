<template>
    <div class="login">
        <Header></Header>

        <section class="login-main">
            <h1>登录</h1>
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="ruleForm.username"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input v-model="ruleForm.password"></el-input>
                </el-form-item>
                <button type="button"　class="submit" @click="submitForm('ruleForm')">登录</button>
            </el-form>
        </section>

    </div>
</template>

<script>
    import Header from './common/Header'
    export default {
        name: "Login",
        components: {
            Header
        },
        data() {
            return {
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'},
                        {min: 2, max: 8, message: '用户名无效', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur' },
                        {min: 3, max: 10, message: '密码错误', trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            /**
             * 登录状态展示
             *
             * @param  {Array} [message, type]
             */
            showLoginStatus([message, type]) {
                this.$message({
                    message: message,
                    type: type
                });
            },


            /**
             * 登录表单提交
             *
             * @param  formName 表单名
             */
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        axios.post(`/login/verify/`,this.ruleForm).then((response) => {
                            let parameter = [];
                            if (response.data === 0) {
                                parameter = ['用户名不存在', 'error'];
                            } else if (response.data === 2) {
                                parameter = ['密码错误', 'error'];
                            } else {
                                parameter = ['登录成功', 'success'];
                            }
                            this.showLoginStatus(parameter);
                            if (response.data === 1) {
                                window.location.href = '/';
                            }
                        }).catch(function (error) {
                            console.log(error);
                        });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }
</script>

<style>
    .login {}


    .login .login-main {
        position: absolute;
        width: 700px;
        top: 50%;
        left: 50%;
        transform: translateX(-50%) translateY(-48%);
        border: 2px solid red;
        border-radius: 8px;
        padding-right: 20px;
    }

    .login h1 {
        font-size: 22px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 12px;
    }

    .login .submit {
        position: relative;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 40px;
        background: #16b5f4;
        border: none;
        border-radius: 8px;
        margin-bottom: 12px;
        font-weight: 600;
        font-size: 16px;
        text-align: center;
        color: white;
    }

</style>