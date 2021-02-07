<template>

  <div class="card-body h-100">
    <div class="row">
      <div class="col mt-0">
        <h6 class="card-title">
          Анкета от {{format_date(ethical_item.created)}}
        </h6>
      </div>

      <div class="row">
        <p>{{ethical_item.employee}}</p>

        <p>Должность: {{ethical_item.employee_position}}</p>

        <p>Статус:
          <span v-if="ethical_item.status === 0" class="badge bg-danger">Новая</span>
          <span v-if="ethical_item.status === 1" class="badge bg-warning">Требует действий</span>
          <span v-if="ethical_item.status === 2" class="badge bg-success">Завершено</span>
        </p>
      </div>
      <div class="row" style="align-content: flex-end">
        <nuxt-link :to="`/ethical/${ethical_item.id}`" class="btn btn-sm btn-light">Подробнее</nuxt-link>
      </div>
      <!--            </div>-->
    </div>
  </div>
</template>

<script>
    import moment from 'moment';

    export default {
        name: "EthicalListItem",
        props: {
            ethical_item: Object
        },
        methods: {
            format_date(value) {
                if (value) {
                    return moment(String(value)).format('DD.MM.YYYY')
                }
            }
        }
    }
</script>

<style scoped>

</style>
