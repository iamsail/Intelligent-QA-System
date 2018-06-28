<template>
    <div class="qa">
        <main>
            <header>与AI聊天中</header>
            <section id = "qaBody">

                <Question
                   :question = 'question'
                ></Question>

                <Answer
                    :answer = 'answer'
                ></Answer>

                <div v-for = "item in QA">
                    <Question
                        :question = 'item.que'
                    ></Question>
                    <Answer
                        :answer = 'item.ans'
                    ></Answer>
                </div>

            </section>
            <footer>
                <input
                        v-model.trim = "askMsg"
                        type="text"
                        placeholder="问点什么..."
                        @keyup.enter="ask()">
            </footer>
        </main>
    </div>
</template>

<script>
    import Question from './Question'
    import Answer from './Answer'
    export default {
        name: "QA",
        components: {
            Question,
            Answer
        },
        data() {
            return {
                question: '我是智能AI机器人,小矿...　正在紧张开发中',
                answer: '哎呦,不错哦',
                askMsg: '',
                QA: []
            }
        },
        methods: {
            ask() {
                let temp = {
                    que: '',
                    ans: ''
                };

                temp.que = this.askMsg;
                this.askMsg = '';



                axios.get('/app/ask')
                    .then((response) => {
                        temp.ans = response.data;
                        if (temp.ans) {
                            this.QA.push(temp);
                        }
                    })
                    .catch( (error) => {

                    });
            }

        }
    }
</script>

<style scoped>
    .qa {
        box-shadow: 0 0 30px 0 rgba(34,195,170,0.5);
        position: relative;
        left: 50%;
        width: 370px;
        height: 90vh;
        transform: translateX(-50%);
        margin-top: 5vh;
        border-radius: 20px;
        background: skyblue;
    }

    .qa main header {
        width: 100%;
        background: white;
        border-radius: 20px 20px 0px 0px;
        height: 40px;
        line-height: 40px;
        text-align: center;
        color: #CCCCCC;
    }

    .qa main footer {
        width: 100%;
        position: absolute;
        border-radius: 0px 0px 20px 20px;
        height: 60px;
        line-height: 60px;
        bottom: 0;
        background: white;
    }

    .qa section {
        margin-left: 8px;
        padding-right: 8px;
        overflow: auto;
        max-height: calc(90vh - 100px);
    }

    .qa footer {}

    .qa footer input {
        border: none;
        height: 30px;
        margin-right: 12px;
        margin-left: 12px;
        width: 90%;
        color: #383434;
    }

    .qa footer input:focus {
        outline: -webkit-focus-ring-color auto 5px;
        outline-color: white;
        outline-style: auto;
        outline-width: 5px;
    }



    ::-webkit-scrollbar {
        width: 5px;
        height: 10px;
    }


    /*滑块*/
    ::-webkit-scrollbar-thumb {
        background-color: #B5F8EC;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: #777;
    }


    /*滑道*/
    ::-webkit-scrollbar-track {#B5F8EC
        box-shadow: inset 0 0 6px #B5F8EC;
        border-radius: 10px;
    }
</style>