<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <BranchList></BranchList>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import BranchList from "~/components/branches/branches-list";

export default {
  components: {
    Logo, Menu, Footer, BranchList
  }
}
</script>

<style>
</style>
