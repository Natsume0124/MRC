import random
from zhipuai import ZhipuAI

def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    """
    Evaluates the submission for a particular challenge phase and returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']

        Example: A sample submission metadata can be accessed like this:
        >>> print(kwargs['submission_metadata'])
        {
            'status': u'running',
            'when_made_public': None,
            'participant_team': 5,
            'input_file': 'https://abc.xyz/path/to/submission/file.json',
            'execution_time': u'123',
            'publication_url': u'ABC',
            'challenge_phase': 1,
            'created_by': u'ABC',
            'stdout_file': 'https://abc.xyz/path/to/stdout/file.json',
            'method_name': u'Test',
            'stderr_file': 'https://abc.xyz/path/to/stderr/file.json',
            'participant_team_name': u'Test Team',
            'project_url': u'http://foo.bar',
            'method_description': u'ABC',
            'is_public': False,
            'submission_result_file': 'https://abc.xyz/path/result/file.json',
            'id': 123,
            'submitted_at': u'2017-03-20T19:22:03.880652Z'
        }
    """
    output = {}
    if phase_codename == "VG-RS":
        print("Evaluating for VG-RS Phase")
        client = ZhipuAI(api_key=API_KEY)
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": "system", "content": "你是一个智能判断助手，你的任务是根据问题和给出的正确答案，分析模型的预测答案是是否正确回答了问题。如果正确，请回答1；如果错误，请回答0；注意，只能输出0或者1，不允许有任何其他内容输出。正确的预测必须完全符合标准答案的语义，否则被认为错误"},
                {"role": "user", "content": "问题是飞机在天上飞？;模型的预测答案是：是的}；正确答案是：是"}
            ],
            temperature=0.0,
        )
        is_true = response.choices[0].message.content
        output["result"] = [
            {
                "train_split": {
                    # "Metric1": random.randint(0, 99),
                    # "Metric2": random.randint(0, 99),
                    # "Metric3": random.randint(0, 99),
                    "ACC": int(9999000) + int(is_true),
                }
            }
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for Dev Phase")
    elif phase_codename == "VQA-SA":
        print("Evaluating for VQA-SA Phase")
        output["result"] = [
            {
                "train_split": {
                    # "Metric1": random.randint(0, 99),
                    # "Metric2": random.randint(0, 99),
                    # "Metric3": random.randint(0, 99),
                    "ACC": int(999999999),
                }
            },
            # {
            #     "test_split": {
            #         # "Metric1": random.randint(0, 99),
            #         # "Metric2": random.randint(0, 99),
            #         # "Metric3": random.randint(0, 99),
            #         "ACC": int(1009999),
            #     }
            # },
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for VQA-SA Phase")
    elif phase_codename == "VR-Ads":
        print("Evaluating for VR-Ads Phase")
        output["result"] = [
            {
                "train_split": {
                    # "Metric1": random.randint(0, 99),
                    # "Metric2": random.randint(0, 99),
                    # "Metric3": random.randint(0, 99),
                    "ACC": int(999999999),
                }
            },
            # {
            #     "test_split": {
            #         # "Metric1": random.randint(0, 99),
            #         # "Metric2": random.randint(0, 99),
            #         # "Metric3": random.randint(0, 99),
            #         "ACC": int(1009999),
            #     }
            # },
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for VR-Ads Phase")
    return output
