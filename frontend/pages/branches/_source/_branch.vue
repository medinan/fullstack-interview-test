<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <BranchDetail v-bind:source="source" v-bind:branch="branch"></BranchDetail>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import BranchDetail from "~/components/branches/branches-detail";

export default {
  components: {
    Logo, Menu, Footer, BranchDetail
  },
  async asyncData({ params}) {
    const source = params.source
    const branch = params.branch
    return { source, branch }
  }
}
</script>

<style>
</style>
