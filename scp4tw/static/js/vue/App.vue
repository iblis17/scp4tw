<template lang="pug">
  section.section
    .container
      // .columns
      //   .column.is-2

      // nav.menu
      //   ul.menu-list
      //     li
      //       a.is-active
      //         span.icon
      //           i.fa.fa-home
      //         | Home
      .box
        p.control.has-addons.has-addons-centered
          input.input(
            placeholder="SCP number"
            v-model="scpNo")
          a.button.is-primary(
            v-on:click="opencc") OpenCC
        p.has-text-centered {{ url }}
      .box.opencc-box
        p.has-text-centered(v-if="openccURL === ''") 你在想尛？
        object(
          v-if="openccURL !== ''"
          type="text/html"
          v-bind:data="openccURL")
</template>

<script>
import $ from 'jquery'


export default {
  data() {
    return {
      scpNo: '',
      openccURL: '',
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
  methods: {
    opencc() {
      if (this.scpNo === '')
        return

      this.openccURL = `/opencc/${this.scpNo}/`

      const box = $('.opencc-box')
      box.height($('body').height() - $('.box').first().height() - 190)
    },
  },
}
</script>

<style>
html, body, section {
  height: 100%;
}
</style>

<style scoped>
div.columns {
  margin-top: 20px;
}
object {
  width: 100%;
  height: 100%;
}
</style>
