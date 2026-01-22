import replicate

def generate_image(prompt: str, output_path="generated.webp") -> str:
    output = replicate.run(
        "sundai-club/boba_img_generator:1c932d8ea15409fe6fa9a9dcf79d1ba952cad3e28375597c63e18e232014e731",
        input={
            "model": "dev",
            "prompt": prompt,
            "go_fast": False,
            "lora_scale": 1,
            "megapixels": "1",
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "guidance_scale": 3,
            "output_quality": 80,
            "prompt_strength": 0.8,
            "extra_lora_scale": 1,
            "num_inference_steps": 28
        }
    )

    # FIX: output is a list, need to access the first element
    with open(output_path, "wb") as f:
        f.write(output[0].read())

    return output_path