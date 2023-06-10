import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	server:{port:3000},
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
};

export default config;
