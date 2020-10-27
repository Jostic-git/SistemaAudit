<template>
  <div class="container">
    <b-navbar toggleable="md" type="light" variant="faded">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Новости</b-nav-item>
          <b-nav-item-dropdown text="О компании">
            <b-dropdown-item to="/about">О компании</b-dropdown-item>
            <b-dropdown-item @click.prevent="showParam" href="#">Еще о чем-то</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item to="/contact">Контакты</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Поиск"></b-form-input>
            <b-button @click.prevent="search" size="sm" class="my-2 my-sm-0" type="submit">Поиск
            </b-button>
            <div style="padding-left: 10px">
              <b-button v-b-modal.modal-prevent-closing size="sm" class="my-2 my-sm-0">
                Написать нам
              </b-button>

            </div>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
    export default {
        name: "navbar"
    }
</script>

<style scoped>

</style>
