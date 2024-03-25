<script setup lang="ts">
import { object, string, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'

const schema = object({
    email: string().email('Invalid email').required('Required'),
    firstName: string().required('Required'),
    lastName: string().required('Required'),
    password1: string()
        .min(8, 'Must be at least 8 characters')
        .required('Required'),
    password2: string()
        .min(8, 'Must be at least 8 characters')
        .required('Required')
})

type Schema = InferType<typeof schema>

const state = reactive({
    email: undefined,
    firstName: undefined,
    lastName: undefined,
    password1: undefined,
    password2: undefined
})

async function onSubmit(event: FormSubmitEvent<Schema>) {
    // Do something with event.data
    console.log(event.data)
}
</script>

<template>
    <UContainer class="flex justify-center">
        <UCard class="size-96">
            <p>Thank you and welcome to LegalCiter.com! If you already have an account please log in <NuxtLink
                    class="text-blue-500 hover:text-blue-500 hover:underline" to="/login">here!</NuxtLink>
            </p>
        </UCard>
        <UCard class="size-96 h-auto ml-6">
            <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
                <UFormGroup label="Email" name="email">
                    <UInput v-model="state.email" />
                </UFormGroup>

                <UFormGroup label="First Name" name="firstName">
                    <UInput v-model="state.email" />
                </UFormGroup>

                <UFormGroup label="Last Name" name="lastName">
                    <UInput v-model="state.email" />
                </UFormGroup>

                <UFormGroup label="Password" name="password1">
                    <UInput v-model="state.password1" type="password1" />
                </UFormGroup>

                <UFormGroup label="Confirm Password" name="password2">
                    <UInput v-model="state.password2" type="password2" />
                </UFormGroup>

                <UButton type="submit">
                    Submit
                </UButton>
            </UForm>
        </UCard>
    </UContainer>
</template>