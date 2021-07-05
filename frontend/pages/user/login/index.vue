<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <Login></Login>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import Login from "~/components/users/Login";

export default {
  components: {
    Logo, Menu, Footer, Login
  }
}
</script>

<style>
</style>
