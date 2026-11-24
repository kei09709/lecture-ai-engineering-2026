# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase': 'Amazon S3 versioning overview', 'topics': ['general']})
- 気づき・疑問：

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 
- やったこと：mcp_servers.jsonに、server.tool()(tools.get_lecture_summary)の記載を追記した。
- 結果：「第2回では何を学びますか？」という質問に対して、glossary_get_lecture_summaryというツールが呼び出されて使用された。
- 気づき・疑問：MCPサーバー側でツールを公開するだけで、エージェント側のコードを変更せずに新しいツールを利用できることが分かった。エージェントが起動時にMCPサーバーからツール一覧を取得する仕組みにより、ツールの管理とエージェントの実装を分離できると理解した。
