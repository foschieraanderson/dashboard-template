<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    
</script>
<template>
  <div class="min-h-svh flex min-w-full bg-red-300">
      <div class="lg:w-2/3">
          <div class="h-full flex justify-center items-center bg-gradient-to-tr from-indigo-400 from-10% to-indigo-500 to-90% hidden lg:flex">
              <div class="flex flex-col gap-6">
                  <div class="flex flex-col gap-2">
                      <h2 class="text-center text-zinc-800 font-bold text-4xl">Registre-se na plataforma</h2>
                      <p class="text-center text-xl text-gray-200 font-normal">Para descobrir um novo mundo cheio de possibilidades</p>
                  </div>
                  <img src="../../assets/register_draw.svg" />
              </div>
          </div>
      </div>
      <div class="w-full lg:w-1/3 bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
          <div class="relative py-3 sm:max-w-xl sm:mx-auto">
            <div
              class="absolute inset-0 bg-gradient-to-r from-indigo-400 to-pink-500 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl">
            </div>
            <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">

              <div class="max-w-md mx-auto">
                <div class="relative flex flex-col gap-8 items-center">
                  <p class="text-4xl font-black">BRAND.</p>
                  <h1 class="text-2xl font-semibold">Quero me registrar</h1>
                </div>
                <div class="divide-y divide-gray-200">
                  <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                    <div class="relative">
                      <input autocomplete="off" id="email" name="email" type="text" class="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-purple-600" placeholder="E-mail" />
                      <label for="email" class="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm">E-mail</label>
                    </div>
                    <div class="relative">
                      <input autocomplete="off" id="password" name="password" type="password" class="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-purple-600" placeholder="Senha" />
                      <label for="password" class="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm">Senha</label>
                    </div>
                    <div class="relative">
                      <input autocomplete="off" id="password-confirm" name="password-confirm" type="password" class="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-purple-600" placeholder="Confirmar Senha" />
                      <label for="password-confirm" class="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm">Confirmar Senha</label>
                    </div>
                    <div class="relative w-full flex justify-center">
                      <button type="submit" class="w-full bg-indigo-300 text-white rounded-md px-2 py-2 mt-2 transition-all hover:bg-indigo-400 hover:scale-105 focus:outline-none">Registrar</button>
                    </div>
                  </div>
                </div>
              </div>

              <div class="relative w-full flex flex-col items-start gap-2">
                  <RouterLink class="text-sm text-gray-400 transition-all hover:underline hover:text-gray-500" :to="{name: 'login'}">Entrar</RouterLink>
              </div>

            </div>
          </div>
      </div>
  </div>
</template>
<style scoped>
    
</style>
