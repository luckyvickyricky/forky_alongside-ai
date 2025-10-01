import requests
import json


BASE_URL = "http://localhost:8000/api/v1"


def main():
    print("Forky AI Interview System - Simple Workflow Example")
    print("=" * 60)
    
    print("\n1. Health Check")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.json()['status']}")
    
    print("\n2. Document Parsing (Skipped - requires PDF file)")
    print("   POST /documents/parse with PDF file")
    
    html_content = """
    <h1>My Portfolio</h1>
    <h2>Project: E-commerce Platform</h2>
    <p>Developed using React, Node.js, and MongoDB</p>
    <p>Implemented user authentication and payment system</p>
    """
    
    print("\n3. Keyword Extraction")
    response = requests.post(
        f"{BASE_URL}/keywords/extract",
        json={
            "html_content": html_content,
            "max_keywords": 5
        }
    )
    
    if response.status_code == 200:
        keywords = response.json()['keywords']
        print(f"Keywords: {keywords}")
    else:
        print(f"Error: {response.status_code}")
        return
    
    print("\n4. Question Generation")
    response = requests.post(
        f"{BASE_URL}/questions/generate",
        json={
            "html_content": html_content,
            "keywords": keywords,
            "num_questions": 3
        }
    )
    
    if response.status_code == 200:
        questions = response.json()['questions']
        print(f"Generated {len(questions)} questions:")
        for i, q in enumerate(questions, 1):
            print(f"  {i}. [{q['category']}] {q['question_text']}")
        
        if questions:
            main_question = questions[0]['question_text']
            
            print("\n5. Simulate User Answer")
            user_answer = "I used React for the frontend and implemented state management with Redux."
            print(f"User: {user_answer}")
            
            print("\n6. Answer Evaluation")
            response = requests.post(
                f"{BASE_URL}/questions/evaluate",
                json={
                    "question": main_question,
                    "answer": user_answer,
                    "context": html_content
                }
            )
            
            if response.status_code == 200:
                feedback = response.json()['feedback']
                print(f"Score: {feedback['score']}/10")
                print(f"Strengths: {', '.join(feedback['strengths'][:2])}")
                print(f"Suggestions: {', '.join(feedback['suggestions'][:2])}")
            
            print("\n7. Following Question Generation")
            response = requests.post(
                f"{BASE_URL}/questions/following",
                json={
                    "question": main_question,
                    "answer": user_answer,
                    "context": html_content
                }
            )
            
            if response.status_code == 200:
                following_q = response.json()['following_question']
                print(f"Following question: {following_q}")
    
    print("\n8. Overall Evaluation")
    response = requests.post(
        f"{BASE_URL}/evaluate/all",
        json={
            "qa_pairs": [
                {
                    "question": "Tell me about your React project",
                    "answer": "I built an e-commerce platform using React"
                },
                {
                    "question": "What technologies did you use?",
                    "answer": "React, Node.js, MongoDB, and Redux"
                }
            ],
            "portfolio_context": html_content
        }
    )
    
    if response.status_code == 200:
        evaluation = response.json()['evaluation']
        print(f"Total Score: {evaluation['total_score']}/100")
        print(f"Technical Competence: {evaluation['technical_competence']}")
    
    print("\n9. Portfolio Evaluation")
    response = requests.post(
        f"{BASE_URL}/evaluate/portfolio",
        json={"html_content": html_content}
    )
    
    if response.status_code == 200:
        evaluation = response.json()['evaluation']
        print(f"Completeness: {evaluation['completeness_score']}/10")
        print(f"Technical Depth: {evaluation['technical_depth_score']}/10")
        print(f"Presentation: {evaluation['presentation_score']}/10")
    
    print("\n" + "=" * 60)
    print("Workflow completed!")


if __name__ == "__main__":
    main()

