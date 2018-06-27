<template>
    <div class="qa">
        <main>
            <header>与AI聊天中</header>
            <section>

                <div class="line">
                    <div class="common question">很高兴遇见你</div>
                </div>

                <div class="line">
                    <div class="common answer">哎呦,不错哦</div>
                </div>

            </section>
            <footer>
                <input type="text" placeholder="说点什么...">
            </footer>
        </main>
    </div>
</template>

<script>
    export default {
        name: "QA",
        data() {
            return {
            
            }
        },
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

    .qa section .line {
        margin-top: 14px;
    }

    .qa section .common {
        display: inline-block;
        min-width: 30px;
        max-width: 280px;
        min-height: 38px;
        line-height: 22px;
        font-size: 14px;
    }

    .qa section .question {
        background: white;
        color: #383434;
        padding: 5px 15px;
        border-radius: 60px/20px 40px 70px 100px;
    }

    .qa section .answer {
        background: white;
        color: #383434;
        padding: 5px 15px;
        float: right;
        border-radius: 10px 30px 70px;
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