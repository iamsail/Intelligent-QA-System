<template>
    <div class="answer">
        <div class="line">
            <div class="ans">{{msg}}</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Answer",
        props:["answer"],
        data() {
            return {
                msg: ''
            };
        },
        methods: {

        },
        mounted(){
            this.msg = this.answer;
        }
    }
</script>

<style scoped>
    .answer {
        display: flex;
        justify-content: flex-end;
    }


    .answer  .line {
        margin-top: 14px;
    }

    .answer  .ans {
        display: inline-block;
        min-width: 30px;
        max-width: 280px;
        min-height: 38px;
        line-height: 22px;
        font-size: 14px;
        background: white;
        color: #383434;
        padding: 5px 15px;
        float: right;
        border-radius: 10px 30px 70px;
        word-break: break-all;
    }

</style>