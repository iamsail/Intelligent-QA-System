<template>
    <div>
        <h1>come on</h1>
        <example></example>
        <h2>{{test}}</h2>
        <h2>{{test1}}</h2>
    </div>
</template>

<script>
    import example from './ExampleComponent'
    import axios from 'axios'
    export default {
        name: "App",
        data() {
            return {
                msg: 'software-cup.',
                test: '666',
                test1: '',
            }
        },
        components: {
            example
        },
        methods: {
            orz() {
                axios.get('/test')
                    .then( (response)  =>{
                        console.log(response);
                                this.test = response.data.key;
                                this.test1 = response.data.db[0].answer;
                    })
                    .catch( (error) => {

                    });
            }
        },
        mounted(){
            this.orz();
        }
    }
</script>

<style scoped>
    .hello {
        font-size: 2em;
        color: green;
    }
</style>