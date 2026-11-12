# Make the coolest art

Entry for the [make.fun](https://make.fun) bounty **coolest-art-01** — "Make the coolest art".

## What it does

`main.py` copies the bundled picture (`art.png` — a phoenix of fire and
electric-blue feathers soaring over a neon cyberpunk city at dusk)
byte-for-byte to `/output/entry.png`. The program uses no network and is
fully deterministic: every run writes identical bytes.

## Run it

```sh
python3 main.py
# writes /output/entry.png (736x736 PNG, under 1 MiB)
```

## License

MIT — see `LICENSE`.
