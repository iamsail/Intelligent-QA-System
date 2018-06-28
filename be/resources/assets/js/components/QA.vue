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
            </section>


            <footer>
                <input
                        v-model.trim = "askMsg"
                        type="text"
                        placeholder="说点什么..."
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
                question: '很高兴遇见',
                answer: '哎呦,不错哦',
                askMsg: ''
            }
        },
        methods: {
            ask() {
                let askMsg = this.askMsg;
                this.askMsg = '';
                let qa = document.querySelector('#qaBody');
                console.log(askMsg);
                console.log(qa);

                let outterDiv = document.createElement("div");
                outterDiv.setAttribute('class', 'line');

                let innerDiv = document.createElement("div");
                innerDiv.setAttribute('class', 'common question');
                innerDiv.innerText = Q;

                outterDiv.appendChild(innerDiv);
                qa.appendChild(outterDiv);

                // axios.get('/app/ask')
                //     .then((response) => {
                //
                //     })
                //     .catch( (error) => {
                //
                //     });
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
        margin-top: 12px;
        margin-left: 8px;
        margin-right: 8px;
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
</style>