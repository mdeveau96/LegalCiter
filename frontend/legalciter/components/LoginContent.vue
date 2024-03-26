<script setup lang="ts">
import { object, string, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'

const schema = object({
    email: string().email('Invalid email').required('Required'),
    password: string()
        .min(8, 'Must be at least 8 characters')
        .required('Required')
})

type Schema = InferType<typeof schema>

const state = reactive({
    email: undefined,
    password: undefined
})

async function onSubmit(event: FormSubmitEvent<Schema>) {
    // Do something with event.data
    console.log(event.data)
}

const isOpen = ref(false)
</script>

<template>
    <UContainer class="flex justify-center pt-6">
        <UCard class="size-96">
            <p>Thank you and welcome to LegalCiter.com! If you do not have an account please create on <NuxtLink
                    class="text-blue-500 hover:text-blue-500 hover:underline" to="/signup">here!</NuxtLink>
            </p>
        </UCard>
        <UCard class="size-96 ml-6">
            <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
                <UFormGroup label="Email" name="email">
                    <UInput v-model="state.email" placeholder="Enter your email" />
                </UFormGroup>

                <UFormGroup label="Password" name="password">
                    <template #hint>
                        <a class="text-blue-500 hover:text-blue-500 hover:underline hover:cursor-pointer"
                            @click="isOpen = true">Forgot password?</a>
                    </template>
                    <template #default>
                        <UInput v-model="state.password" type="password" placeholder="Enter your password" />
                    </template>
                </UFormGroup>

                <UButton type="submit">
                    Submit
                </UButton>

                <UModal v-model="isOpen">
                    <div class="p-4 justify-center">
                        <div class="w-14 mx-auto">
                            <a href="/">
                                <img src="/law-firm-icon-13.png" class="h-14">
                            </a>
                        </div>
                        <h1 class="font-lg text-center py-2">Reset your password</h1>
                        <UCard>
                            <UForm>
                                <UFormGroup
                                    label="Enter your user account's verified email address and we will send you a password reset link."
                                    name="email">
                                    <UInput v-model="state.email" placeholder="Enter your email" />
                                </UFormGroup>
                            </UForm>
                        </UCard>
                    </div>
                </UModal>
            </UForm>
        </UCard>
    </UContainer>
</template>