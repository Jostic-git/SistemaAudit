<template>
  <select v-model="values" class="form-select" :disabled="!isActive" @change="sendValue()">
    <option v-bind:value="null" selected>Выберите значение</option>
    <option v-bind:value="true">Да</option>
    <option v-bind:value="false">Нет</option>
  </select>

</template>

<script>
    export default {
        name: "SelectYesNo",
        data() {
            return {
                values: Boolean
            }
        },
        props: {
            isActive: Boolean,
            values: Boolean

        },
        methods: {
            sendValue(){
              console.log(this.values)
              // this.$emit('update-value', this.values)
            }
        }
    }
</script>

<style scoped>

</style>
