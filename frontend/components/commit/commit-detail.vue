<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>BRANCHES</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="/">Home</a>
            <a class="breadcrumb-item" href="/branches/">Branches</a>
            <a class="breadcrumb-item" :href="'/branches/' + source + '/' + branch">{{ source }}/{{ branch }}</a>
            <a class="breadcrumb-item active" href="#">{{ commit }}</a>
          </nav>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">hash</th>
              <th scope="col">message</th>
              <th scope="col">author</th>
              <th scope="col">email</th>
              <th scope="col">date</th>
              <th scope="col">files</th>
            </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{details.hash}}</td>
                <td>{{details.message}}</td>
                <td>{{details.author}}</td>
                <td>{{details.email}}</td>
                <td>{{details.date}}</td>
                <td>{{details.files}}</td>
              </tr>

            </tbody>
          </table>
          <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>

  export default {
    name: "CommitDetail",
    props: ["source", "branch", "commit"],
    mounted: function () {
      this.getCommits();
    },
    data: function () {
      return {
        details: []
      }
    },
    methods: {
      getCommits: function () {
        const url = "/api/v1/branches/" + this.source + "_" + this.branch + "/commits/" + this.commit
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          self.details = response.data;
        })
      }
    }
  }
</script>

<style scoped>

</style>
