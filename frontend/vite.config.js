import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import mkcert from 'vite-plugin-mkcert';

export default defineConfig({
	plugins: [mkcert(), sveltekit()],
	server:{port:3000},
	ssr: {
		noExternal: ['three']
	}
});
