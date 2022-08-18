FROM quantiledevelopment/vscode-python-azure:3.9

# Install python packages in the repo itself
RUN poetry config virtualenvs.in-project true 

# Install Meltano
RUN pipx install meltano