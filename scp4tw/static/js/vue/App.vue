<template lang="pug">
  .container
    .columns
      .column.is-2
        nav.menu
          ul.menu-list
            li
              a.is-active
                span.icon
                  i.fa.fa-home
                | Home
      .column
        .box
          p.control.has-addons.has-addons-centered
            input.input(
              placeholder="SCP number"
              v-model="scpNo")
            a.button.is-primary OpenCC
          p.has-text-centered {{ url }}
</template>

<script>
export default {
  data() {
    return {
      scpNo: undefined,
    }
  },
  computed: {
    url() {
      const base = 'http://scp-wiki-cn.wikidot.com/scp-'

      if (! this.scpNo )
        return base

      return `${base}${this.scpNo}`
    },
  },
}
</script>

<style>
</style>

<style scoped>
div.columns {
  margin-top: 20px;
}
</style>
