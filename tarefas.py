import streamlit as st

def main():
    st.title('Lista de Tarefas')

    # Carrega a lista de tarefas existente ou cria uma nova lista
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

    # Entrada de nova tarefa
    new_task = st.text_input('Adicione uma nova tarefa:', '')
    st.write('Exemplo: Limpar a casa')
    
    # Botão para adicionar tarefa
    if st.button('Adicionar Tarefa'):
        if new_task:  # Adiciona a tarefa se a entrada não estiver vazia
            st.session_state['tasks'].append({'task': new_task, 'completed': False})
            new_task = ''  # Limpa o campo de entrada

    # Mostra as tarefas atuais
    if st.session_state['tasks']:
        for i, task_info in enumerate(st.session_state['tasks']):
            col1, col2 = st.columns([0.8, 0.2])
            task_text = f"{'✓' if task_info['completed'] else ''} {task_info['task']}"
            col1.text(task_text)
            
            # Botão para marcar tarefa como concluída
            if not task_info['completed']:
                if col2.button('Concluir', key=f'complete_{i}'):
                    st.session_state['tasks'][i]['completed'] = True
    else:
        st.write("Nenhuma tarefa adicionada ainda.")

if __name__ == "__main__":
    main()
