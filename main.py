from engine.example import example
from engine.iou import IOUengine
from engine.bounding_box import BoundingBox
import gradio as gr


bounding_box = BoundingBox()
iou = IOUengine()


def clear_inputs_and_outputs() -> list:
    """
    Clears all inputs and outputs when the user clicks "Clear" button
    """
    return ""


# Input: image_path (str)
# Output: ground_box (image), tess_box (image), matching_percentage (float)
# For: draw bounding box from groundtruth and tesseract to find matching percentage
# OEM working list : 1 3
# PSM working list : 1 3 4 5 6 7 8 9 10 11 12
def process_image(image_path):
    oem = 3
    psm = 3
    ground_box = bounding_box.draw_boxes_from_groundtruth(image_path)
    tess_box = bounding_box.run_tesseract(image_path, oem, psm, "eng+tha")
    both_box = bounding_box.draw_both_boxes(image_path, oem, psm, "eng+tha")
    matching_percentage, image_iou = iou.runiou(
        image_path, oem, psm, "eng+tha")

    return ground_box, tess_box, both_box, matching_percentage, image_iou


with gr.Blocks() as my_demo:
    with gr.Row():
        with gr.Column():
            upl_input = gr.Image(
                type="pil",
                label="Select a file",
            )
            image_path = gr.Textbox(
                label="Image Path",
            )

            with gr.Row():
                sub_btn = gr.Button(value="Submit Benchmark")
                clr_btn = gr.Button(value="Clear", variant="secondary")

            gr.Examples(
                label="Demo images",
                examples=example,
                inputs=[upl_input, image_path],
            )

        with gr.Row():
            with gr.Column():
                matching_percentage = gr.Textbox(
                    label="Area Matching Percentage")
                gr.Markdown(f"Tesseract output")
                ground_box = gr.Image()
                gr.Markdown(f"GroundTruth output")
                tess_box = gr.Image()
                gr.Markdown(f"Draw both box")
                both_box = gr.Image()
                gr.Markdown(f"IOU box")
                iou_box = gr.Image()
        clr_btn.click(
            fn=clear_inputs_and_outputs,
            inputs=[],
            outputs=[],
        )

        sub_btn.click(fn=process_image, inputs=[
                      image_path], outputs=[ground_box, tess_box, both_box, matching_percentage, iou_box])


my_demo.launch(server_name="0.0.0.0", server_port=8000)