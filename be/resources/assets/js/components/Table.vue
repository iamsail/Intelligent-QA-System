<template>
    <div class="QA-table">
        <section>
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
        </section>
        <section class="cut-page">
            <div class="block">
                <el-pagination
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page="currentPage"
                        :page-sizes="[100, 200, 300, 500, 1000]"
                        :page-size="100"
                        layout="total, sizes, prev, pager, next, jumper"
                        :total="QANums">
                </el-pagination>
            </div>
        </section>
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
              axios.get(`/QA?pageSize=${this.pageSize}`)
                  .then((response)  =>{
                      let QA = response.data;
                      this.QANums = QA.total;
                      this.dataPath = `${QA.path}?page=`;
                      this.renderTableQA(QA.data);
                  })
                  .catch( (error) => {

                  });
          },

          /**
           * 将QA对渲染到页面
           *
           * @param data 将QA对数据渲染到页面
           */
          renderTableQA(data) {
            data.forEach((val) => {
              this.tableData.push(val);
            })
          },


          /**
           * 改变每个页面的显示的QA对数量
           *
           * @param val 每页展示多少条数据
           */
          handleSizeChange(val) {
              this.pageSize = val;
              this.getQA();
          },


          /**
           * 页面跳转
           *
           * @param val 跳转的页码
           */
          handleCurrentChange(val) {
              let url = `${this.dataPath}${val}&pageSize=${this.pageSize}`;
              axios.get(url)
                  .then((response)  =>{
                     this.tableData = [];
                     this.renderTableQA(response.data.data);
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
                tableData: [],
                currentPage: 1,
                QANums: 0,
                dataPath: '',
                pageSize: 100
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

    .QA-table .cut-page {
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .QA-table .el-pagination {
        text-align: center;
    }
</style>
