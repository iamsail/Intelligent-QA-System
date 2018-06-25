<template>
    <div class="QA-table">
        <el-table
                :data="tableData"
                stripe
                style="width: 80%">
            <el-table-column
                    prop="id"
                    align="center"
                    label="问题id"
                    width="180">
            </el-table-column>
            <el-table-column
                    prop="question"
                    align="center"
                    label="问题"
                    width="180">
            </el-table-column>
            <el-table-column
                    prop="theme"
                    align="center"
                    label="主题">
            </el-table-column>
            <el-table-column
                    prop="answer"
                    align="center"
                    label="答案">
            </el-table-column>
            <el-table-column
                    prop="answer_link"
                    align="center"
                    label="答案链接">
            </el-table-column>
            <el-table-column
                    prop="extend_question"
                    align="center"
                    label="扩展问题">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    export default {
        name: "Table",
        methods: {
          getQA() {
              axios.get('/QA')
                  .then( (response)  =>{
                      let QA = response.data.QA;
                      QA.forEach((val) => {
                        this.tableData.push(val);
                        console.log(val)
                      })
                  })
                  .catch( (error) => {

                  });
          }
        },
        mounted() {
            this.getQA();
        },
        data() {
            return {
                tableData: []
            }
        }
    }
</script>

<style>
    .QA-table .el-table {
        margin: 0 auto;
    }
</style>
