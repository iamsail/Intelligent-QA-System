<template>
    <div>
        <h1>come on</h1>
        <example></example>
    </div>
</template>

<script>
    import example from './ExampleComponent'
    export default {
        name: "App",
        data() {
            return {
                msg: 'software-cup.'
            }
        },
        components: {
            example
        }
    }
</script>

<style scoped>
    .hello {
        font-size: 2em;
        color: green;
    }
</style>