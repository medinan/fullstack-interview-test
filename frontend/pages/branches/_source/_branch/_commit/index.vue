<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <CommitDetail v-bind:source="source" v-bind:branch="branch" v-bind:commit="commit"></CommitDetail>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import CommitDetail from "~/components/commit/commit-detail";

export default {
  components: {
    Logo, Menu, Footer, CommitDetail
  },
  async asyncData({ params}) {
    const source = params.source
    const branch = params.branch
    const commit = params.commit
    return { source, branch, commit }
  }
}
</script>

<style>
</style>
