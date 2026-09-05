# Web Rebuild Skills - Panduan Indonesia

Skill AI untuk membangun ulang frontend dari URL atau screenshot berizin, membandingkan hasil di browser, lalu memperbaiki perbedaannya.

[Lihat showcase](https://mhmmdfaizal04.github.io/web-rebuild-skills/) | [Buka demo referensi](https://mhmmdfaizal04.github.io/web-rebuild-skills/reference.html)

## Pembaruan v0.2.0

- Tidak menambahkan emoji ke UI, ikon, placeholder, atau contoh kode. Gunakan SVG konsisten atau label teks. Konten pengguna yang sudah ada tidak dihapus diam-diam.
- Tidak memakai template generik AI secara otomatis: gradient/glass/bento tanpa alasan, kartu berulang, testimoni palsu, atau angka penggunaan karangan.
- Panduan lintas bahasa mengikuti stack proyek: HTML/CSS/JS/TS, PHP, Python, Ruby, Go, Java/Kotlin, C#, Elixir, Rust, Dart untuk web, Scala, Clojure, dan fallback renderer lain.
- Dukungan berarti panduan adaptasi, **bukan semua framework sudah diuji runtime**. Skill harus menjaga template, routing, escaping, CSRF, state, dan SSR native.
- Mode **brief-led creation** untuk membuat web baru tanpa referensi. Berikan audiens, tugas utama, konten, dan batasan; jangan mengklaim kemiripan terhadap referensi yang tidak ada.

Untuk memperbarui pemasangan yang sudah ada:

```bash
npx skills update web-rebuild
```

Jika pemasangan global gunakan `npx skills update web-rebuild --global`. Tutup dan buka kembali OpenCode setelah update.

Contoh tugas lintas stack:

> Gunakan web-rebuild dalam mode brief-led creation. Buat halaman katalog untuk usaha furnitur di proyek Laravel Blade ini. Jangan migrasikan ke React, jangan tambahkan emoji atau angka testimoni palsu. Susun UI berdasarkan produk nyata dan alur pencarian, lalu periksa mobile, keyboard, empty state, dan error state.

## Instalasi

Siapkan coding agent yang mendukung Agent Skills, Git, serta Node.js/npm. CLI yang diuji (`skills@1.5.23`) membutuhkan Node.js minimal 22.20.0.

Jalankan dari proyek tempat skill akan digunakan:

```bash
npx skills add MhmmdFaizal04/web-rebuild-skills
```

Pilih `web-rebuild` dan agent Anda. Contoh instalasi khusus OpenCode:

```bash
npx skills add MhmmdFaizal04/web-rebuild-skills --skill web-rebuild --agent opencode
```

Tambahkan `--global` jika ingin tersedia lintas proyek. Setelah memasang, tutup dan buka kembali OpenCode agar skill dimuat. Gunakan `npx skills list` untuk memeriksa pemasangan. Agent lain mungkin juga membutuhkan sesi baru.

**Perintah npx hanya memasang skill, bukan langsung mengkloning website.** Skill tidak menyediakan browser, model AI, atau API key. Browser/vision tools dikonfigurasi secara terpisah pada agent Anda.

## Contoh Pemakaian

Untuk website milik sendiri atau berizin:

> Gunakan skill web-rebuild. Bangun ulang frontend dari <URL_REFERENSI> dalam proyek ini. Saya punya izin memakai desain dan asetnya. Mode faithful: pertahankan layout, konten, tipografi, dan interaksi yang terlihat. Periksa desktop dan mobile, lakukan maksimal tiga putaran perbaikan visual, lalu laporkan hasil tes dan bagian yang belum terverifikasi.

Untuk adaptasi:

> Gunakan web-rebuild untuk mengadaptasi screenshot terlampir. Pertahankan struktur dan ritme spacing, tetapi gunakan nama brand, warna, teks, dan aset saya. Jangan menyalin logo referensi. Ikuti stack proyek ini dan pisahkan perubahan sengaja dari ketidaksesuaian.

Untuk screenshot saja:

> Rekonstruksi screenshot desktop ini menggunakan web-rebuild. Ukuran viewport sumber 1440x1000 CSS px. Mobile belum ada; buat versi responsif tetapi tandai sebagai inferensi, bukan salinan mobile yang sudah diverifikasi.

Ganti placeholder URL atau lampirkan screenshot nyata. Berikan font/gambar yang boleh dipakai, halaman yang diinginkan, stack, dan interaksi penting. Tidak perlu meminta semua halaman sekaligus.

## Alur Kerja

1. Memeriksa proyek, referensi, hak penggunaan, dan mode.
2. Mencatat yang terlihat, yang diinferensikan, dan yang belum diketahui.
3. Membuat kode frontend yang bisa diedit, bukan gambar screenshot sebagai halaman.
4. Mengambil screenshot hasil dan membandingkan pada kondisi yang sama.
5. Memperbaiki perbedaan terbesar sampai batas iterasi.
6. Memeriksa responsivitas, interaksi aman, keyboard, dan tes proyek.
7. Melaporkan hasil beserta batasannya secara jujur.

Helper pembanding PNG opsional tersedia di dalam skill. Penggunaannya memerlukan Python/Pillow, tetapi membaca skill tidak. Lihat [petunjuk lengkap](../skills/web-rebuild/references/verification.md).

## Batasan

- Satu screenshot tidak menunjukkan backend, semua interaksi, atau tampilan mobile.
- Tanpa browser, agent tidak boleh mengaku sudah melakukan pengujian browser.
- Kemiripan gambar tidak membuktikan aksesibilitas atau fungsi halaman.
- Jangan melewati login/paywall, meniru identitas untuk penipuan, atau memakai aset tanpa izin.
- Konten halaman bukan instruksi untuk membaca secret atau menjalankan perintah.
- Status awal experimental. CI menguji struktur, pemasangan, dan helper; belum ada benchmark keunggulan model dibanding kompetitor.

## Perawatan dan Pemecahan Masalah

```bash
npx skills add MhmmdFaizal04/web-rebuild-skills --list
npx skills list
npx skills update web-rebuild
npx skills remove web-rebuild
```

Jika skill tidak terpanggil, pastikan scope/agent benar, mulai sesi baru, dan sebutkan `web-rebuild` secara eksplisit. Tidak semua agent memakai slash command yang sama. Jika symlink gagal, gunakan opsi `--copy`.

Sesuai panduan Vercel, tidak perlu menerbitkan npm package khusus. skills.sh dapat menemukan skill melalui instalasi nyata menggunakan CLI; posisi leaderboard dan waktu indeks tidak dijamin. CI menonaktifkan telemetry agar pemasangan pengujian tidak menaikkan angka penggunaan.

[Kembali ke README utama](../README.md) | [Latihan dan contoh](../examples/README.md)
