<template>
    <fwb-navbar>
        <template #logo>
            <router-link to="/" class="font-bold text-3xl text-blue-900 tracking-tight">
                <img src="../assets/law-firm-icon-13.png" class="h-10 w-10 inline-flex">
                LegalCiter
            </router-link>
        </template>
        <template #default="{isShowMenu}">
        <fwb-navbar-collapse :is-show-menu="isShowMenu">
            <fwb-navbar-link is-activ   e>
            <router-link to="/">Home</router-link>
            </fwb-navbar-link>
            <fwb-navbar-link>
            <router-link to="/about">About</router-link>
            </fwb-navbar-link>
        </fwb-navbar-collapse>
        </template>
        <template #right-side>
            <router-link to="/signup" class="pt-2">
                <fwb-button class="bg-blue-900 p-2">
                    Sign Up
                </fwb-button>
            </router-link>
        <fwb-navbar-collapse>
            <fwb-navbar-link>
                <router-link to="/login">Log In</router-link>
            </fwb-navbar-link>
        </fwb-navbar-collapse>
        </template>
    </fwb-navbar>
</template>
  
<script setup>
    import {
        FwbButton,
        FwbNavbar,
        FwbNavbarCollapse,
        FwbNavbarLink,
    } from 'flowbite-vue'
import { RouterLink } from 'vue-router'
</script>
