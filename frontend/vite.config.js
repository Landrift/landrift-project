// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  root: 'src',  // srcディレクトリをプロジェクトのルートとする
  server: {
    host: '0.0.0.0',
    port: 3001,
    strictPort: true,
    open: false,
  },
});
