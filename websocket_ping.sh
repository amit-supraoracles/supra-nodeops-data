for i in {1..10}; do
  echo "Hello, WebSocket!" | ws ws://localhost:8000
done
