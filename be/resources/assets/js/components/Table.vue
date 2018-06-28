<template>
    <div class="QA-table">
        <el-table
                :data="tableData"
                stripe
                border
                style="width: 100%">
            <el-table-column
                    prop="id"
                    align="center"
                    label="问题id"
                    width="80">
            </el-table-column>
            <el-table-column
                    prop="question"
                    align="center"
                    label="问题"
                    width="240">
            </el-table-column>
            <el-table-column
                    prop="theme"
                    align="center"
                    width="200"
                    label="主题">
            </el-table-column>
            <el-table-column
                    prop="answer"
                    align="center"
                    width="350"
                    label="答案">
            </el-table-column>
            <el-table-column
                    prop="answer_link"
                    width="350"
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
        props:["arrQA"],
        methods: {
          /**
           * 获取QA对
           */
          getQA() {
              axios.get('/QA')
                  .then( (response)  =>{
                      let QA = response.data.QA;
                      QA.forEach((val) => {
                        this.tableData.push(val);
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
        /*margin: 0 auto;*/
    }

    @keyframes typing {
        0% {
            white-space:nowrap;
        }

        100% {
            white-space:normal;
        }
    }

    .QA-table .el-table tbody .cell {
        white-space:nowrap;
        text-overflow:ellipsis;
        min-height: 30px;
    }

    .QA-table .el-table tbody .cell:hover {
        animation: typing .1s .5s ease-out both;
        animation-fill-mode: forwards;
    }
</style>
