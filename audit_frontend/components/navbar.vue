<template>
  <div class="container">
    <b-navbar toggleable="md" type="light" variant="faded">
      <b-navbar-toggle target="nav-collapse"/>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">
            Новости
          </b-nav-item>
          <b-nav-item-dropdown text="Справочники">
            <b-dropdown-item to="/companies">
              Активы (организации)
            </b-dropdown-item>
            <b-dropdown-item href="#" @click.prevent="showParam">
              Риски
            </b-dropdown-item>
            <b-dropdown-item href="#" @click.prevent="showParam">
              Процессы
            </b-dropdown-item>
            <b-dropdown-item href="#" @click.prevent="showParam">
              Пользователи
            </b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item to="/card">
            Карта гарантий
          </b-nav-item>
          <b-nav-item to="/card">
            Проекты
          </b-nav-item>

          <b-nav-item-dropdown text="Горячая линия">
            <b-dropdown-item to="/hotline/newitem">
              Добавить обращение
            </b-dropdown-item>
            <b-dropdown-item to="/hotline/">
              Журнал обращений
            </b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="Этическая аттестация">
            <b-dropdown-item to="/ethical/newform/">
              Добавить анкету
            </b-dropdown-item>
            <b-dropdown-item to="/ethical/">
              Журнал анкет
            </b-dropdown-item>
          </b-nav-item-dropdown>

        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Поиск"/>
            <b-button size="sm" class="my-2 my-sm-0" type="submit" @click.prevent="search">
              Поиск
            </b-button>

            <div style="padding-left: 10px">
              <b-button v-if="!isAuth" size="sm" class="my-2 my-sm-0" type="submit" @click.prevent="checkAuth()">
                Login
              </b-button>
              <b-button v-if="isAuth" size="sm" class="my-2 my-sm-0" type="submit" @click.prevent="checkAuth()">
                LogOut
              </b-button>
            </div>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
    const Cookie = process.client ? require('js-cookie') : undefined;

    export default {
        name: 'Navbar',
        methods: {
            search() {
                console.log('this.isAuth() ', this.isAuth)
            },
            async checkAuth() {
                if (!this.isAuth)
                    this.$router.push("/auth/")
                else {
                    try {
                        this.$axios.setToken(this.isAuth, 'Token');
                        await this.$axios.$post('/auth/token/logout');
                        this.$axios.setToken(false)
                        Cookie.remove('tokenS')
                        this.$store.commit('setAuth', null)
                    } catch
                        (e) {
                        console.log(e);
                    }

                }
            }
        },
        computed: {
            isAuth() {
                return this.$store.state.auth
            }
        },
        mounted() {
            var cook = Cookie.get('tokenS');
            if (cook) {
                this.$store.commit('setAuth', cook);
            }
        }
    }
</script>

<style scoped>

</style>
