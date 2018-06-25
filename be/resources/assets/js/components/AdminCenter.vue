<template>
    <div class="admin-center">
        <h1>控制中心</h1>
        <section class="controller">
            <div>
                <el-popover
                        placement="top"
                        width="160"
                        v-model="visible">
                    <p>确定清空所有QA对吗?</p>
                    <div style="text-align: right; margin: 0">
                        <el-button size="mini" type="text" @click="visible = false">取消</el-button>
                        <el-button type="primary" size="mini" @click="clearQA()">确定</el-button>
                    </div>
                    <el-button type="danger" slot="reference">清空QA对</el-button>
                </el-popover>
            </div>

            <div>
                <el-button type="success" @click="dialogFormVisible = true">新增QA对</el-button>
                <el-dialog title="收货地址" :visible.sync="dialogFormVisible">
                    <el-form :model="form">
                        <el-form-item label="活动名称" :label-width="formLabelWidth">
                            <el-input v-model="form.name" auto-complete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="活动区域" :label-width="formLabelWidth">
                            <el-select v-model="form.region" placeholder="请选择活动区域">
                                <el-option label="区域一" value="shanghai"></el-option>
                                <el-option label="区域二" value="beijing"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-form>
                    <div slot="footer" class="dialog-footer">
                        <el-button @click="dialogFormVisible = false">取 消</el-button>
                        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                    </div>
                </el-dialog>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: "AdminCenter",
        data() {
            return {
                visible: false,

                dialogFormVisible: false,
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                formLabelWidth: '120px'
            };
        },
        methods: {
            refresh() {
                window.location.href = '/';
            },
            clearQA() {
                this.visible = false;
                axios.delete('/QA/all/')
                    .then((response)  =>{
                        this.refresh();
                    })
                    .catch((error) => {

                    });
            }
        },

    }
</script>

<style scoped>
    .admin-center {}

    .admin-center h1{
        background: skyblue;
        text-align: center;
        margin: 0 auto;
        height: 36px;
        line-height: 36px;
        color: white;
        font-weight: 600;
    }

    .admin-center .controller {
        margin-top: 5px;
    }

    .admin-center .controller div {
        display: inline-block;
        margin-left: 3px;
    }
</style>