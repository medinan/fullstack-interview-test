<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>ADD PULL REQUESTS</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="/">Home</a>
            <a class="breadcrumb-item" href="/pullrequests/">Pull requests</a>
            <span class="breadcrumb-item active">Add</span>
          </nav>
          <div class="row mb80">
            <div class="col-sm-4 offset-sm-4">
                <form method="post" @submit.prevent="createPullRequest">
                  <div class="form-group">
                    <label for="pullrequest-form-title">Title</label>
                    <input v-model="form.title" type="text" class="form-control" name="title" id="pullrequest-form-title" required>
                  </div>
                  <div class="form-group">
                    <label for="pullrequest-form-author">Author</label>
                    <input v-model="form.author" type="text" class="form-control" name="author" id="pullrequest-form-author" required>
                  </div>
                  <div class="form-group">
                    <label for="pullrequest-form-base">Branch base</label>
                    <select v-model="form.branch_base"  class="custom-select" aria-label="Default select example" name="base" id="pullrequest-form-base" required>
                      <option v-for="branch in branches" v-bind:value="branch.source + '/' + branch.name">{{branch.source}}/{{branch.name}}</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="pullrequest-form-compare">Branch compare</label>
                    <select v-model="form.branch_compare" class="custom-select" aria-label="Default select example" name="compare" id="pullrequest-form-compare" required>
                      <option v-for="branch in branches" v-bind:value="branch.source + '/' + branch.name">{{branch.source}}/{{branch.name}}</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="pullrequest-form-status">Status</label>
                    <select v-model="form.status" class="custom-select" aria-label="Default select example" name="status" id="pullrequest-form-status" required>
                      <option v-for="state in status" v-bind:value="state.value">{{ state.text }}</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="login-form-description">Description</label>
                    <textarea v-model="form.description" type="te" class="form-control" name="description" id="login-form-description" required></textarea>
                  </div>
                  <!-- /.form-group -->
                  <button type="submit" class="btn btn-primary pull-right">Create</button>
                </form>
            </div>
            <!-- /.col-sm-4 -->
          </div>
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
    name: "PullRequestAdd",
    mounted: function () {
      this.getBranches();
    },
    data: function () {
      return {
        branches: [],
        status: [
          {value: "open", text: "open"},
          {value: "merged", text: "merged"},
        ],
        form: {
          title: "",
          author: "",
          branch_base: "",
          branch_compare: "",
          status: "open",
          description: ""
        }
      }
    },
    methods: {
      getBranches: function () {
        const url = "/api/v1/branches/"
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          self.branches = response.data;
        })
      },
      createPullRequest: function () {
        const url = "/api/v1/pullrequests/"
        let self = this;
        let params = this.form;
        this.$axios.post(url, params, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
            self.$router.push("/pullrequests/")
        })
      },
    }
  }
</script>

<style scoped>

</style>
